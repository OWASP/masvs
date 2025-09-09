# MASVS-RESILIENCE: Resilience Against Reverse Engineering and Tampering

Defense-in-depth measures such as code obfuscation, anti-debugging, anti-tampering, and runtime application self-protection (RASP) can increase an app's resilience against reverse engineering and specific client-side attacks. They add multiple layers of security controls to the app, making it more difficult for attackers to modify code or extract sensitive information.

**The absence of these measures does not in itself constitute a vulnerability**. Instead, resilience controls provide additional protection against threat-specific attacks. **All apps must also fulfill the rest of the OWASP MASVS** controls according to their threat model.

## Business and Commercial Perspective

Resilience measures are particularly relevant when the app needs to protect business assets or deter client-side abuse. They can help mitigate risks such as:

- Theft or compromise of proprietary algorithms, trade secrets, customer data, AI or machine learning models  
- Fraud, cheating, or revenue leakage in online games, financial apps, or subscription models  
- Legal and reputational damage due to breach of contracts or regulations  
- Damage to brand reputation due to negative publicity or customer dissatisfaction

These controls aim to ensure the app is running on a trusted platform, detect or prevent tampering at runtime, and preserve the integrity of the app's intended functionality.

## Transparency and Open Audit Perspective

In some contexts, such as government, health, or other public-interest apps, resilience measures may not be ideal due to multiple reasons:

- It reduces transparency of what the compiled application is doing  
- Independent verification of the compiled application is more difficult  
- The diversity of smartphone operating systems can lead to false positives, potentially excluding legitimate users

In case these concerns are valid for the target application, we recommend applying the following principles:

- Open source distribution of source code for independent audits  
- Security must rely on verifiable design, strong cryptography, and server-side validation  
- Anti-tampering or obfuscation techniques must not be used as a substitute for proper security architecture  
- Controls should prevent cheating or malicious modification without hindering legitimate analysis or oversight

## Platform/Developer lock-in

Runtime resilience controls focus on two things:

- The application and its own memory and files  
- The underlying OS

While verifying the integrity of the application itself is typically OS-agnostic, the same cannot be said for verifying the underlying OS. For example, while there is an open-source version of Android (AOSP), this is typically not the OS that is installed on consumer devices. Instead, many different flavors are developed with small differences in feature sets and security controls. Some examples include Google Android, HarmonyOS, FireOS, LineageOS, /e/OS, etc. By implementing flavor-specific detection mechanisms, the application may not function on any other flavor of Android. This results in a platform lock-in, possibly excluding legitimate users from using the application.  

Additionally, reliance on platform services such as Google Play Integrity API or Apple's App Attestation may further reinforce lock-in and limit accessibility for certain user groups.

## Malware and Testing Perspective

Resilience techniques can also be abused by malicious software. Malware authors often use code obfuscation, anti-debugging, and anti-tampering to:

- Conceal malicious functionality  
- Evade security tools or app store review  
- Frustrate researchers and hinder forensic analysis

For this reason, security testers must understand these techniques, know how to detect them, and practice bypassing them. This ensures that security assessments remain effective, and that defensive controls are distinguished from attempts to conceal harmful behavior.
