# Contributing to Ironcreed

> *"Only through unity of purpose can we withstand the darkness."*

## Deployment Protocols

Thank you for your interest in strengthening the Ironcreed arsenal. All contributions help fortify our defenses against the digital void.

## Code of Conduct

By participating in this project, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md). We maintain discipline and mutual respect in our ranks.

## How to Contribute

### Reporting Issues

Found a vulnerability in the defenses? Report it:

1. Search existing issues to avoid duplicates
2. Use a clear, descriptive title
3. Provide detailed reproduction steps
4. Include system specifications
5. Add relevant logs or error messages

### Submitting Changes

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Ironcreed.git
   cd Ironcreed
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-enhancement
   # or
   git checkout -b fix/your-bugfix
   ```

3. **Follow the Standards**
   - Write clear, defensive code
   - Add tests for new functionality
   - Update documentation
   - Ensure all tests pass
   - Follow existing code style

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   Use clear commit messages:
   - `feat: Add new authentication system`
   - `fix: Resolve memory leak in cache layer`
   - `docs: Update security guidelines`
   - `test: Add integration tests for API`

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-enhancement
   ```
   
   Then open a pull request with:
   - Clear description of changes
   - Reference to related issues
   - Test results
   - Any breaking changes noted

## Development Guidelines

### Security First
- Never commit secrets, keys, or credentials
- Validate all inputs
- Sanitize all outputs
- Assume hostile environments
- Defense in depth

### Code Quality
- Write self-documenting code
- Add comments for complex logic
- Keep functions focused and small
- Prefer explicitness over cleverness
- Error handling is mandatory

### Testing
- Unit tests for business logic
- Integration tests for systems
- Security tests for vulnerabilities
- Load tests for performance-critical code

### Documentation
- README for each tool/system
- API documentation for interfaces
- Architecture decisions recorded
- Security considerations documented

## Review Process

1. Automated checks must pass
2. Code review by maintainers
3. Security review if applicable
4. Documentation review
5. Merge upon approval

## Questions?

Open an issue with the `question` label or reach out through existing discussions.

---

*Through discipline and vigilance, we prevail.*
