# Mobile Application Security Model

The MAS project defines several security testing profiles that businesses and developers can use to evaluate and improve the security of their mobile applications. However, it’s important to note that implementing these profiles fully or partially should be a risk-based decision made in consultation with business owners.

![MAS Profiles](images/masvs-levels-new.jpg)\

**MAS-L1 - Baseline Security:**

MAS-L1 contains generic security controls recommended for all mobile apps. This profile considers co-installed apps as well as network-based attackers but assumes that the security controls of the mobile operating system are intact and that the end user is not viewed as a potential adversary. Fulfilling these controls results in a secure app that follows best practices and avoids common vulnerabilities.

**MAS-L2 - Defense-in-Depth:**

MAS-L2 adds additional defense-in-depth controls to protect against more sophisticated attacks. This profile assumes that the security controls of the mobile operating system might not be intact and that the app user can be considered as a potential adversary. It is appropriate for apps handling highly sensitive data, such as mobile banking apps.

**MAS-R - Resilience:**

MAS-R contains software protection controls to impede specific client-side threats where the end user is malicious and/or the mobile OS is compromised. These threats include tampering, modding, or reverse engineering to extract sensitive code or data. This level is applicable to apps that need to protect intellectual property such as gaming apps and enterprise apps that handle confidential or proprietary information.

**Note that MAS-R controls can ultimately be bypassed and should never be used as a replacement for proper security controls. Instead, they are intended to add additional threat-specific protective controls to apps that also fulfill the MASVS controls in MAS-L1 or MAS-L2.**

## Recommended Use

A risk assessment should be the first step before applying the MASVS. Apps can be verified against the different MAS profiles based on prior risk assessment and overall level of security required which will determine which MAS profile or profiles should be applied to the app. Note that combinations of profiles are possible:

- MAS-L1
- MAS-L1 + MAS-R
- MAS-L2
- MAS-L2 + MAS-R

The different combinations reflect different grades of security and resilience. Threat model is essential to determine not only the profiles to be applied but also the controls and risks (represented by tests in the MASTG) that are applicable. **When testing using a MAS profile you don't have to apply each and every test**

The goal is to allow for flexibility: For example, a mobile game might not warrant adding MAS-L2 security controls such as 2-factor authentication for usability reasons, but have a strong business need for tamper prevention.

## The Security Trade-offs

Adding more security controls from higher MAS profiles can make the app more secure, but it also may increase the cost of development and may affect the user experience negatively.

### Security vs Cost

In general, MAS profiles should be used whenever it makes sense from a risk vs. cost perspective (i.e., where the potential loss caused by a compromise of confidentiality or integrity is higher than the cost incurred by the additional security controls). The potential loss is the negative impact that a compromise of confidentiality or integrity would have on the app's users, data, functionality, reputation, or revenue. The cost of security controls is the amount of time, money, and resources that are needed to implement and maintain the security features. You need to estimate how likely it is that your app will be attacked, how severe the consequences would be if your app's data was compromised, and how much value your app provides to your users and your business.

For example, if you are developing a mobile app that handles sensitive health data of your users, you might want to use MAS-L2 to ensure strong encryption and authentication features. The potential loss caused by a data breach would be very high in terms of user privacy, trust, and legal liability. The cost of implementing these security controls would be justified by the value and reputation of your app.

On the other hand, if you are developing a mobile app that only displays public information such as weather forecasts or news articles, complying with MAS-L1 is usually enough. The potential loss caused by a data breach would be low in terms of user privacy and trust. The cost of implementing these security controls would not be worth the marginal benefit for your app.

### Security vs Usability

Some security features may make the app more difficult or inconvenient to use, which may affect user satisfaction or retention. For example, requiring complex passwords or frequent verification may increase security, but also frustrate users who want a smooth and fast experience. Developers should predict and resolve conflicts between security and usability requirements during the app design process.

### Security vs Privacy

Some security features may require accessing or collecting user data, which may raise privacy concerns. For example, using SMS as multi-factor authentication may improve security, but also expose sensitive personal information (the user telephone number). Developers should balance the security and privacy needs of their users and comply with relevant laws and regulations.

### Privacy vs Value

Some apps may offer more value or functionality to users in exchange for accessing or sharing their data, which may compromise their privacy. For example, some apps may provide personalized recommendations or discounts based on user preferences or location data, but also expose users to targeted ads or third-party tracking. Developers should be aware that users will weigh the benefits and risks of downloading and using such apps based on their own privacy concerns.

## Examples of Use

### MASVS-L1

- All mobile apps. MASVS-L1 lists security best practices that can be followed with a reasonable impact on development cost and user experience. Apply the controls in MASVS-L1 for any app that don't qualify for one of the higher levels.

### MASVS-L2

- Health-Care Industry: Mobile apps that store personally identifiable information that can be used for identity theft, fraudulent payments, or a variety of fraud schemes. For the US healthcare sector, compliance considerations include the Health Insurance Portability and Accountability Act (HIPAA) Privacy, Security, Breach Notification Rules and Patient Safety Rule.

- Financial Industry: Apps that enable access to highly sensitive information like credit card numbers, personal information, or allow the user to move funds. These apps warrant additional security controls to prevent fraud. Financial apps need to ensure compliance to the Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Act and Sarbanes-Oxley Act (SOX).

### MASVS L1+R

- Mobile apps where Intellectual Property (IP) protection is a business goal. The resilience controls listed in MASVS-R can be used to increase the effort needed to obtain the original source code and to impede tampering / cracking.

- Gaming Industry: Games with an essential need to prevent modding and cheating, such as competitive online games. Cheating is an important issue in online games, as a large amount of cheaters leads to a disgruntled player base and can ultimately cause a game to fail. MASVS-R provides basic anti-tampering controls to help increase the effort for cheaters.

### MASVS L2+R

- Financial Industry: Online banking apps that allow the user to move funds, where techniques such as code injection and instrumentation on compromised devices pose a risk. In this case, controls from MASVS-R can be used to impede tampering, raising the bar for malware authors.

- All mobile apps that, by design, need to store sensitive data on the mobile device, and at the same time must support a wide range of devices and operating system versions. In this case, resilience controls can be used as a defense-in-depth measure to increase the effort for attackers aiming to extract the sensitive data.

- Apps with in-app purchases should ideally use server-side and MASVS-L2 controls to protect paid content. However, there may be cases where there is no possibility to use server-side protection. In those cases, MASVS-R controls should be additionally applied in order to increase the reversing and/or tampering effort.
