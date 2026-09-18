---
hide:
  - toc
---

# OWASP MASVS

<img src="../assets/masvs_cover.png" align="right" style="border-radius: 3px; margin: 3em; box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;" width="350px" >

<a href="https://github.com/OWASP/masvs/">:material-github: GitHub Repo</a>

The **OWASP MASVS (Mobile Application Security Verification Standard)** is the industry standard for mobile app security. It can be used by mobile software architects and developers seeking to develop secure mobile applications, as well as security testers to ensure completeness and consistency of test results.

To complement the MASVS, the OWASP MAS project also provides the [OWASP Mobile Application Security Testing Guide (MASTG)](https://mas.owasp.org/MASTG) and the [OWASP Mobile Application Security Weakness Enumeration (MASWE)](https://mas.owasp.org/MASWE) which together are the perfect companion for verifying the controls listed in the OWASP MASVS and demonstrate compliance.

<br>

<button class="mas-button" onclick="window.location.href='https://github.com/OWASP/masvs/releases/latest/download/OWASP_MASVS.pdf';"> Download the MASVS</button>

<br>

## The MASVS Control Groups

The standard is divided into various groups of controls, labeled **MASVS-XXXXX**, that represent the most critical areas of the mobile attack surface:

- **MASVS-STORAGE**: Secure storage of sensitive data on a device (data-at-rest).
- **MASVS-CRYPTO**: Cryptographic functionality used to protect sensitive data.
- **MASVS-AUTH**: Authentication and authorization mechanisms used by the mobile app.
- **MASVS-NETWORK**: Secure network communication between the mobile app and remote endpoints (data-in-transit).
- **MASVS-PLATFORM**: Secure interaction with the underlying mobile platform and other installed apps.
- **MASVS-CODE**: Security best practices for data processing and keeping the app up-to-date.
- **MASVS-RESILIENCE**: Resilience to reverse engineering and tampering attempts.
- **MASVS-PRIVACY**: Privacy controls to protect user privacy.

<br><br>
