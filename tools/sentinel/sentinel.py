#!/usr/bin/env python3
"""
Sentinel - File Integrity Monitoring Tool
Part of the Ironcreed Arsenal

A defensive tool for monitoring file integrity through cryptographic hashing.
Embodies the principle: "Trust nothing, verify everything."
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set


class Sentinel:
    """File integrity monitoring system"""
    
    BASELINE_FILE = ".sentinel_baseline.json"
    LOG_FILE = "sentinel.log"
    
    def __init__(self, watch_path: str):
        """Initialize Sentinel with a path to monitor"""
        self.watch_path = Path(watch_path).resolve()
        self.baseline_path = self.watch_path / self.BASELINE_FILE
        self.log_path = self.watch_path / self.LOG_FILE
        
        if not self.watch_path.exists():
            raise ValueError(f"Watch path does not exist: {self.watch_path}")
    
    def _log(self, message: str, level: str = "INFO") -> None:
        """Append message to audit log"""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except IOError as e:
            print(f"Warning: Failed to write to log: {e}", file=sys.stderr)
    
    def _hash_file(self, filepath: Path) -> Optional[str]:
        """Calculate SHA-256 hash of file"""
        try:
            hasher = hashlib.sha256()
            with open(filepath, "rb") as f:
                # Read in chunks for memory efficiency
                for chunk in iter(lambda: f.read(8192), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except (IOError, PermissionError) as e:
            self._log(f"Failed to hash {filepath}: {e}", "WARNING")
            return None
    
    def _scan_files(self) -> Dict[str, str]:
        """Scan directory and generate hash map"""
        file_hashes = {}
        
        for root, dirs, files in os.walk(self.watch_path):
            # Skip the baseline and log files themselves
            if self.BASELINE_FILE in files:
                files.remove(self.BASELINE_FILE)
            if self.LOG_FILE in files:
                files.remove(self.LOG_FILE)
            
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                if filename.startswith('.'):
                    continue
                    
                filepath = Path(root) / filename
                relative_path = filepath.relative_to(self.watch_path)
                
                file_hash = self._hash_file(filepath)
                if file_hash:
                    file_hashes[str(relative_path)] = file_hash
        
        return file_hashes
    
    def init(self) -> bool:
        """Initialize baseline snapshot"""
        print(f"Initializing baseline for: {self.watch_path}")
        self._log("Baseline initialization started")
        
        if self.baseline_path.exists():
            response = input("Baseline already exists. Overwrite? (yes/no): ")
            if response.lower() != "yes":
                print("Initialization cancelled.")
                return False
        
        file_hashes = self._scan_files()
        
        baseline = {
            "created": datetime.now().isoformat(),
            "watch_path": str(self.watch_path),
            "file_count": len(file_hashes),
            "files": file_hashes
        }
        
        try:
            with open(self.baseline_path, "w", encoding="utf-8") as f:
                json.dump(baseline, f, indent=2)
            
            # Set restrictive permissions on baseline
            os.chmod(self.baseline_path, 0o600)
            
            print(f"✓ Baseline created: {len(file_hashes)} files monitored")
            self._log(f"Baseline created with {len(file_hashes)} files")
            return True
            
        except IOError as e:
            print(f"✗ Failed to write baseline: {e}", file=sys.stderr)
            self._log(f"Baseline creation failed: {e}", "ERROR")
            return False
    
    def verify(self) -> bool:
        """Verify current state against baseline"""
        if not self.baseline_path.exists():
            print("✗ No baseline found. Run 'init' first.", file=sys.stderr)
            return False
        
        print(f"Verifying integrity: {self.watch_path}")
        self._log("Integrity verification started")
        
        try:
            with open(self.baseline_path, "r", encoding="utf-8") as f:
                baseline = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"✗ Failed to read baseline: {e}", file=sys.stderr)
            self._log(f"Baseline read failed: {e}", "ERROR")
            return False
        
        baseline_files = baseline["files"]
        current_files = self._scan_files()
        
        baseline_set = set(baseline_files.keys())
        current_set = set(current_files.keys())
        
        # Detect changes
        modified = []
        for filepath in baseline_set & current_set:
            if baseline_files[filepath] != current_files[filepath]:
                modified.append(filepath)
        
        added = current_set - baseline_set
        deleted = baseline_set - current_set
        
        # Report results
        issues_found = False
        
        if modified:
            issues_found = True
            print(f"\n⚠ MODIFIED ({len(modified)}):")
            for filepath in sorted(modified):
                print(f"  - {filepath}")
                self._log(f"Modified: {filepath}", "WARNING")
        
        if added:
            issues_found = True
            print(f"\n+ ADDED ({len(added)}):")
            for filepath in sorted(added):
                print(f"  + {filepath}")
                self._log(f"Added: {filepath}", "WARNING")
        
        if deleted:
            issues_found = True
            print(f"\n- DELETED ({len(deleted)}):")
            for filepath in sorted(deleted):
                print(f"  - {filepath}")
                self._log(f"Deleted: {filepath}", "WARNING")
        
        if not issues_found:
            print("\n✓ All files verified. No changes detected.")
            self._log("Verification passed: no changes")
            return True
        else:
            print(f"\n✗ Integrity check failed: {len(modified)} modified, {len(added)} added, {len(deleted)} deleted")
            self._log(f"Verification failed: {len(modified)} modified, {len(added)} added, {len(deleted)} deleted", "WARNING")
            return False
    
    def status(self) -> None:
        """Display monitoring status"""
        print(f"Sentinel Status")
        print(f"Watch Path: {self.watch_path}")
        
        if self.baseline_path.exists():
            try:
                with open(self.baseline_path, "r", encoding="utf-8") as f:
                    baseline = json.load(f)
                print(f"✓ Baseline: {baseline['created']}")
                print(f"  Files monitored: {baseline['file_count']}")
            except (IOError, json.JSONDecodeError) as e:
                print(f"✗ Baseline corrupted: {e}")
        else:
            print("✗ No baseline (run 'init' to create)")
        
        if self.log_path.exists():
            log_size = self.log_path.stat().st_size
            print(f"  Audit log: {log_size} bytes")


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description="Sentinel - File Integrity Monitor (Ironcreed Arsenal)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  sentinel.py init /etc/config       Initialize monitoring
  sentinel.py verify                 Check for changes
  sentinel.py status                 Show current status

The watchful eye that never sleeps.
        """
    )
    
    parser.add_argument(
        "command",
        choices=["init", "verify", "status"],
        help="Command to execute"
    )
    
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to monitor (default: current directory)"
    )
    
    args = parser.parse_args()
    
    try:
        sentinel = Sentinel(args.path)
        
        if args.command == "init":
            success = sentinel.init()
            sys.exit(0 if success else 1)
        
        elif args.command == "verify":
            success = sentinel.verify()
            sys.exit(0 if success else 1)
        
        elif args.command == "status":
            sentinel.status()
            sys.exit(0)
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
