# SF3E Alert

> **Personal Safety Redefined.** A comprehensive mobile emergency alert application that connects you with your emergency contacts instantly.

[![Python](https://img.shields.io/badge/Python-99.3%25-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview

**SF3E Alert** is an intelligent mobile application engineered to provide rapid emergency assistance when personal safety is at risk. The application bridges the critical gap between users in distress and their trusted emergency contacts by enabling one-tap alert activation coupled with real-time location sharing.

Designed with accessibility and speed as core principles, SF3E Alert eliminates friction during emergencies—every second counts. The application leverages modern mobile technologies to ensure reliable delivery of emergency notifications with precise location data.

### Problem Statement

In critical emergency situations, traditional communication methods are often ineffective:
- Phone calls may go unanswered
- Multiple manual contacts consume precious time
- Location information is difficult to convey accurately

SF3E Alert solves these challenges through:
- **Instantaneous Notifications**: One-touch alert distribution to multiple contacts
- **Precise Location Sharing**: Automated GPS location transmission via clickable map links
- **Offline Resilience**: Core functionality available with minimal connectivity

## Key Features

### 🚨 Emergency Alert System
- One-tap activation of emergency protocols
- Simultaneous SMS alerts to multiple pre-configured contacts
- Customizable alert messages with personal context
- Contact management interface for easy updates

### 📍 Real-Time Location Sharing
- Automatic GPS location capture during alert activation
- Google Maps integration for intuitive location sharing
- Live location link embedded in alert messages
- Location history logging for emergency responders

### 🎯 User-Centric Design
- Minimal, intuitive interface optimized for crisis situations
- Large, accessible touch targets for emergency activation
- Dark mode support for low-light environments
- Multi-language support (extensible)

### 🔐 Security & Privacy
- Encrypted storage of emergency contact information
- Secure credential management for SMS services
- Opt-in location sharing with explicit user control
- No collection of non-emergency usage data

### 📱 Cross-Platform Compatibility
- Native support for Android and iOS devices via Kivy framework
- Responsive design adapts to various screen sizes
- Minimal resource footprint for older devices
- Progressive enhancement of features based on device capabilities

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python (99.3%) | Core application logic |
| **UI Framework** | Kivy / KivyMD | Native cross-platform mobile interface |
| **UI Markup** | KV Language (0.7%) | Declarative UI definitions |
| **SMS Service** | Twilio API | Reliable SMS alert delivery |
| **Location Services** | Native GPS / Google Maps API | Location capture & sharing |
| **Database** | SQLite | Local contact & configuration storage |
| **IDE** | PyCharm (recommended) | Development environment |

## System Requirements

### Minimum Requirements
- **OS**: Android 6.0+ / iOS 12.0+
- **RAM**: 512 MB
- **Storage**: 50 MB available space
- **Network**: Active cellular or WiFi connection (SMS delivery)
- **Permissions**: GPS, SMS, Contacts, Network

### Recommended
- **RAM**: 2GB+
- **Storage**: 100 MB
- **OS**: Latest stable Android/iOS version
- **Network**: 4G/5G for optimal performance

## Installation

### For Development

**Prerequisites:**
- Python 3.8 or higher
- pip package manager
- Virtual environment tool (recommended: `venv` or `virtualenv`)
- Git

**Steps:**

1. **Clone the repository**
   ```bash
   git clone https://github.com/anudeep0011/SF3E.git
   cd SF3E
   ```

2. **Create and activate virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

### For Deployment

Build and deploy using Buildozer (recommended for Kivy apps):

```bash
# Install buildozer
pip install buildozer

# Build APK for Android
buildozer android debug

# Build for iOS (macOS only)
buildozer ios debug
```

## Configuration

### 1. Twilio Setup

SF3E Alert uses Twilio for reliable SMS delivery. Configure as follows:

1. Create an account at [twilio.com](https://www.twilio.com)
2. Obtain your credentials:
   - Account SID
   - Auth Token
   - Twilio Phone Number

3. Create/update `config.py` in the project root:

```python
# config.py
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_PHONE_NUMBER = '+1234567890'  # Your Twilio number

# Optional Configuration
ALERT_MESSAGE_TEMPLATE = "Emergency Alert: {name} needs help! Location: {map_link}"
MAX_EMERGENCY_CONTACTS = 10
SMS_TIMEOUT = 30  # seconds
```

### 2. Google Maps API (Optional)

For enhanced map features:

1. Enable Google Maps API in your Google Cloud project
2. Add API key to `config.py`:

```python
GOOGLE_MAPS_API_KEY = 'your_google_maps_api_key'
```

### 3. Environment Variables

Alternatively, configure via environment variables (recommended for production):

```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_PHONE_NUMBER="+1234567890"
```

## Usage

### First-Time Setup

1. **Launch the application**
   ```
   Open SF3E Alert on your device
   ```

2. **Configure emergency contacts**
   - Navigate to Settings/Contacts
   - Add trusted emergency contacts with phone numbers
   - Verify contact information before saving

3. **Grant permissions**
   - GPS/Location services
   - SMS sending capability
   - Contact access (optional)

### Sending an Alert

1. **Trigger emergency mode**
   - Press the prominent **EMERGENCY** button on the main screen
   - Or use accessibility gesture (if enabled)

2. **Confirm alert**
   - Review pre-filled message (optional editing)
   - Confirm recipients
   - Press **SEND ALERT**

3. **Monitor status**
   - View delivery status of each SMS
   - See recipient acknowledgment timeline
   - Access your location via embedded map link

### Managing Contacts

- **Add**: Settings → Contacts → [+] → Enter details
- **Edit**: Settings → Contacts → [Contact] → Modify
- **Remove**: Settings → Contacts → [Contact] → Delete
- **Import**: Settings → Contacts → Import from phone

## Architecture

### System Components

```
┌─────────────────────────────────────────┐
│         SF3E Alert Application          │
├─────────────────────────────────────────┤
│ ┌───────────────────────────────────┐   │
│ │     UI Layer (Kivy/KivyMD)        │   │
│ │  - Main screen                    │   │
│ │  - Settings/Contacts              │   │
│ │  - Alert confirmation             │   │
│ └──────────────┬──────────────────┘   │
│                │                       │
│ ┌──────────────▼──────────────────┐   │
│ │    Business Logic Layer         │   │
│ │  - Contact management           │   │
│ │  - Alert orchestration          │   │
│ │  - Location capture             │   │
│ └──────────────┬──────────────────┘   │
│                │                       │
│ ┌──────────────▼──────────────────┐   │
│ │    Service Layer                │   │
│ │  - GPS service                  │   │
│ │  - SMS service (Twilio)         │   │
│ │  - Notification service         │   │
│ └──────────────┬──────────────────┘   │
│                │                       │
│ ┌──────────────▼──────────────────┐   │
│ │    Data Layer                   │   │
│ │  - Local database (SQLite)      │   │
│ │  - Configuration cache          │   │
│ └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Key Modules

- **`main.py`**: Application entry point and main screen logic
- **`services/sms.py`**: Twilio integration and SMS handling
- **`services/location.py`**: GPS capture and location management
- **`services/contact.py`**: Emergency contact storage and retrieval
- **`database/db.py`**: SQLite database operations
- **`ui/screens.py`**: Kivy screen definitions
- **`utils/config.py`**: Configuration management

## Contributing

We welcome contributions from the community! Whether bug fixes, features, or documentation improvements, your help makes SF3E Alert safer for everyone.

### Contribution Workflow

1. **Fork the repository**
   ```bash
   Click "Fork" on the GitHub page
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clear, descriptive commit messages
   - Follow PEP 8 coding standards
   - Add tests for new functionality
   - Update documentation as needed

4. **Commit and push**
   ```bash
   git commit -m "Add: your feature description"
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Reference any related issues
   - Describe the changes and rationale
   - Ensure all tests pass

### Code Standards

- **Python**: PEP 8 compliance
- **Comments**: Clear docstrings for all functions
- **Testing**: Unit tests for business logic
- **Documentation**: Update README for user-facing changes

### Reporting Issues

Found a bug? Please report it:
1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Device/OS information
   - Relevant logs or screenshots

## Roadmap

### Planned Features (v1.1+)

- [ ] Voice activation for hands-free alerts
- [ ] Wearable device integration (smartwatches)
- [ ] WhatsApp and Telegram notification support
- [ ] Emergency services direct integration (911/999)
- [ ] Automated periodic location check-ins
- [ ] Multi-language support expansion
- [ ] Biometric authentication (fingerprint/face)
- [ ] Offline alert queuing with retry logic

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms and conditions.

```
MIT License

Copyright (c) 2026 SF3E Alert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## Support

### Getting Help

- **Documentation**: See this README and inline code comments
- **Issues**: Check [GitHub Issues](https://github.com/anudeep0011/SF3E/issues) for Q&A
- **Discussions**: Start a conversation in [GitHub Discussions](https://github.com/anudeep0011/SF3E/discussions)

### Emergency Disclaimer

**Important:** SF3E Alert is a supplementary safety tool and should not replace official emergency services. In life-threatening situations, always call emergency services directly:

- **USA**: 911
- **UK**: 999
- **EU**: 112
- **Other**: Contact your local emergency number

### Security Vulnerabilities

If you discover a security vulnerability, please email [security contact] instead of using the issue tracker.

---

<div align="center">

**SF3E Alert: Quick. Reliable. Lifesaving.**

[Report Issue](https://github.com/anudeep0011/SF3E/issues) • [Request Feature](https://github.com/anudeep0011/SF3E/issues) • [View Releases](https://github.com/anudeep0011/SF3E/releases)

</div>
