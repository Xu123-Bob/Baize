# Contributing to Baize

Thank you for your interest in contributing to Baize! We welcome all forms of participation, including reporting issues, submitting code, improving documentation, and making suggestions.

# Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Issues](#reporting-issues)
  - [Submitting Code](#submitting-code)
  - [Development Workflow](#development-workflow)
- [Code Style and Testing](#code-style-and-testing)
- [Commit Message Guidelines](#commit-message-guidelines)
- [License and Contributor License Agreement (CLA)](#license-and-contributor-license-agreement-cla)
  - [Current License](#current-license)
  - [Why We Need a CLA](#why-we-need-a-cla)
  - [Individual Contributors](#individual-contributors)
  - [Corporate Contributors](#corporate-contributors)
  - [How to Sign](#how-to-sign)
  - [Relicensing of Already Merged Contributions](#relicensing-of-already-merged-contributions)
- [Contact](#contact)

# Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be friendly, respectful, and inclusive.

# How to Contribute

## Reporting Issues

- Use GitHub Issues to report bugs or suggest features.
- Search existing issues to avoid duplicates.
- Provide a clear title, reproduction steps, expected behavior, and actual behavior.
- If possible, include environment information and screenshots.

## Submitting Code

1. Fork this repository.

2. Create your feature branch: `git checkout -b feature/your-feature-name`.

3. Commit your changes: `git commit -m "feat: add some feature"`.

4. Push to the branch: `git push origin feature/your-feature-name`.

5. Open a Pull Request on GitHub.

Before submitting a PR, please ensure that:

- The code passes existing tests.
- Relevant documentation has been updated.
- The code style is followed.
- You have read and agreed to the license terms in this document.

## Development Workflow

```bash
# Clone the repository
git clone https://github.com/Xu123-Bob/Baize.git
cd Baize

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-data.txt
```

## Code Style and Testing

- Follow the project's existing code style.
- Add corresponding tests for new features.
- Ensure all tests pass before submitting a PR.
- If the project has lint tools, run them before submitting.

## Commit Message Guidelines

We use the Conventional Commits specification:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

# License and Contributor License Agreement (CLA)

## Current License

This project is currently licensed under the **MIT License**. We reserve the right to adopt other open source licenses in the future, including but not limited to the Apache License 2.0, to better accommodate project development and community needs.

Old versions will be permanently released under the MIT License. Any license changes will only apply to future new versions.

## Why We Need a CLA

To maintain license flexibility for the project and ensure that all contributions have a clear legal basis, we require contributors to sign a **Contributor License Agreement (CLA)**.

Signing the CLA **does not** cause you to lose copyright to your contributions. You still retain copyright; you merely grant the project maintainers a perpetual, worldwide, royalty-free, irrevocable license to distribute and relicense your contributions under the project's current or future licenses.

## Individual Contributors

If you are contributing as an **individual**, please sign the **Individual Contributor License Agreement (ICLA)**. You can sign it in the following ways:

- Directly reply to the CLA bot prompt in the PR.

If you manually confirm in the PR, please reply with the following statement:

```text
I agree to the terms of the Individual Contributor License Agreement (ICLA) and license my contributions under the project's current and future licenses.
```

## Corporate Contributors

If you are contributing on behalf of a **company** or **employer**, and your contributions may be owned by the company, then an authorized company representative must sign the **Corporate Contributor License Agreement (CCLA)**.

The CCLA must be signed by a person authorized to sign legal contracts on behalf of the company, such as legal counsel, executives, or OSS compliance officers. The engineer submitting the PR typically does not have the authority to sign it.

After signing the CCLA, the company must designate a **CLA Manager** and add your GitHub account or email to the authorized contributor list. After that, your contributions will be automatically recognized as covered by the CCLA.

**CCLA Template and Signing Methods:**

- We use the **Apache Foundation CCLA template**.

- Signing methods:

1. Electronic signature: Sign online via [DocuSign / EasyCLA / other tools].

2. Email signature: Download the CCLA PDF, print and sign it, then scan and send it to [826741152@qq.com].

3. PGP signature: Fill out the PDF and use a PGP detached signature, then send the file and signature to [826741152@qq.com].

4. If you are unsure whether corporate signing is required, please contact [826741152@qq.com] first to explain your situation.

Company authorized representative confirmation statement:

```text
On behalf of [Company], we confirm that [Company] owns or has sufficient rights to the contributions submitted by [Name] in [PR/commit IDs], and has authority to grant this permission. We agree to license those contributions under the project's current and future licenses.
```

## How to Sign

- When you submit a PR, the CLA bot will automatically check whether you have signed.
- If you have not signed, the bot will provide a link and guidance.
- Individual contributors sign through the ICLA process.
- Corporate contributors should contact their company's legal/OSS compliance team to sign through the CCLA process and add you to the authorized list.
- After signing is complete, simply re-trigger the PR check.

If you have any questions about the CLA process, please email [826741152@qq.com] or open an Issue in this repository.

## Relicensing of Already Merged Contributions

For contributions that were already merged before this project adopted the CLA, if we need to change the license in the future, we will separately contact the contributors or their companies to obtain explicit consent before relicensing.

We respect every contributor's decision. If we cannot obtain consent for relicensing, we will retain the MIT License or rewrite the relevant code.

## Contact

Project Maintainer: [Xu Xin / GitHub ID]

Email: [826741152@qq.com]

Issue Tracking: [GitHub Issues](https://github.com/Xu123-Bob/Baize/issues)

Thank you again for your contribution!