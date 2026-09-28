# Risk Assessment Report

## 1. Identification of Assets, Vulnerabilities, and Consequences

| Asset | Vulnerability | Possible Consequence |
| :--- | :--- | :--- |
| **1. Student Records Server** | Guest network has direct access to the server. | Unauthenticated guests can gain unauthorized access, alter grades, or exfiltrate sensitive student data. |
| **2. Staff Accounts & Credentials** | Weak staff passwords and lack of MFA. | Attackers can perform brute-force attacks, compromise accounts, and gain administrative control over student records. |
| **3. Inter-Campus File Transfers** | Unencrypted communication channels used for file transfers between campuses. | External attackers or eavesdroppers can perform Man-in-the-Middle (MitM) attacks to intercept or tamper with sensitive files in transit. |

---

## 2. Risk Ranking Matrix

Risks are evaluated based on **Likelihood** (High, Medium, Low) and **Impact** (High, Medium, Low).

| Rank | Risk Description | Likelihood | Impact | Overall Risk Level | Justification |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | **Unauthorized Access via Guest Network** | High | High | **CRITICAL** | Guest access to the records server provides an open vector for anyone connected to the local Wi-Fi. The impact is catastrophic if records are altered or leaked. |
| **2** | **Credential Compromise (Weak Passwords)** | High | High | **HIGH** | Repeated external login attempts have already been observed. Weak passwords make brute-force or dictionary attacks highly likely to succeed soon. |
| **3** | **Inter-Campus Data Interception** | Medium | Medium | **MEDIUM** | Requires an attacker to position themselves on the network path between campuses, but unencrypted traffic is easily readable if intercepted. |

---

## 3. Recommended Controls

1. **Control for Risk 1 (Guest Access to Records Server):**
   * **Network Segmentation & Firewall Rules:** Place the student records server in an isolated VLAN/subnet restricted to administrative staff. Implement strict firewall rules (e.g., `iptables`) to drop all traffic originating from the guest network.

2. **Control for Risk 2 (Weak Staff Passwords):**
   * **Password Policy & Multi-Factor Authentication (MFA):** Enforce strong password complexity rules (minimum 12 characters, mixing case, digits, and symbols) and mandate Multi-Factor Authentication (MFA) for all staff account logins.

3. **Control for Risk 3 (Unencrypted File Transfers):**
   * **Transport Security Protocol:** Replace all unencrypted file transfer protocols (e.g., FTP, HTTP) with secure encrypted protocols such as SFTP (SSH File Transfer Protocol) or HTTPS (TLS 1.3).
