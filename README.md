# 🔐 FortiBlock: Hybrid Blockchain Framework for Secure Access Control in Cloud Environment 🛡️
[![Blockchain](https://img.shields.io/badge/Blockchain-Ethereum-blue)](https://ethereum.org/)
[![Security](https://img.shields.io/badge/Security-AES%20%7C%20SHA--256-green)](https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment)
[![Status](https://img.shields.io/badge/Status-KSCST%20Sponsored-orange)](https://kscst.org.in/spp.html)
[![Cloud](https://img.shields.io/badge/Cloud-Security-yellow)](https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment)

<!-- Add Project Logo/Banner Image Here -->
<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/Main_Pic.png" alt="FortiBlock Banner" width="850px">
</div>

## 🎉 Award Recognition
We are thrilled to share that FortiBlock has been **selected for sponsorship** under the **48th Series of Student Project Programme (SPP) 2024-25** by the **Karnataka State Council for Science and Technology (KSCST)**! 

<div align="center">
  <blockquote>
    Among numerous Deep Learning and Machine Learning projects, FortiBlock stood out as the only Blockchain-based project selected for sponsorship.
  </blockquote>
</div>

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Architecture](#️-architecture)
- [Technology Stack](#-technology-stack)
- [Implementation Details](#-implementation-details)
- [Security Mechanisms](#-security-mechanisms)
- [Results and Demonstrations](#-results-and-demonstrations)
- [Applications](#-applications)
- [Future Scope](#-future-scope)
- [Team Members](#-team-members)
- [Project Documentation](#-project-documentation)
- [Acknowledgements](#-acknowledgements)
- [Contact](#-contact)

## 🔍 Project Overview
FortiBlock is a blockchain-powered security framework designed to provide two-way data protection and secure access control for cloud environments. Traditional centralized cloud access control systems are prone to single points of failure, insider threats, and lack of transparency, making them vulnerable to data breaches and unauthorized modifications.

Our project addresses these challenges by integrating blockchain technology, cryptographic security, and scalable cloud infrastructure to enhance data protection and implement decentralized access management.

## ✨ Key Features
- **Decentralized Access Control**: Tamper-proof blockchain storage of access rights with blockchain account addresses serving as user identities
- **Hybrid Blockchain Architecture**: Combines public blockchain transparency with private blockchain confidentiality
- **End-to-End Encryption**: AES encryption for data security before cloud storage
- **Secure Authentication**: SHA-256 hashing for user credential protection
- **Role-Based Access Control (RBAC)**: Automated permission grants, revocations, and monitoring through smart contracts
- **Immutable Access Logs**: Blockchain-based storage of metadata, transaction logs, and access records
- **Direct & Indirect Sharing**: Support for various data sharing models with security controls
- **Access Revocation**: Real-time revocation of permissions with cascade effect

## 🏗️ Architecture
FortiBlock employs a unique hybrid blockchain architecture with the following workflow:

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/architecture.png" alt="Architecture Flow" width="750px">
</div>

1. **Data Owner Upload**: Resources are uploaded to cloud storage
2. **Cloud Verification**: Validation of uploaded data
3. **Permission Publishing**: Access permissions and authorizations recorded on blockchain
4. **User Resource Requests**: Data users request access to resources
5. **Request Validation**: Verification of user requests
6. **Permission Querying**: Blockchain verification of permissions
7. **Access Response**: Blockchain confirms or denies access
8. **Resource Delivery**: Providing access to authorized users
9. **Access Logging**: Recording all access activities on blockchain

## 💻 Technology Stack

<div align="center">

| Component | Technologies |
|:-------------:|:-------------:|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Django, Node.js |
| **Blockchain** | Ethereum, Solidity Smart Contracts, Web3.js |
| **Encryption** | AES (Advanced Encryption Standard) |
| **Authentication** | SHA-256/512 Hashing |
| **Cloud Storage** | IPFS API |
| **Data Structures** | Merkle Trees, Mapping, Linked Lists, Hash Tables |

</div>

## 🔧 Implementation Details

### Modules
1. **User Interface Module (UI)**
   - Data Owner UI for registration, login, and file uploading
   - Data User UI for requesting access and downloading shared data
   - Access Revocation UI for permission management

2. **Authentication and Authorization Module**
   - Login and Registration with encrypted credential storage
   - Role-Based Access Control (RBAC) implementation
   - Secure hash key generation using SHA-512

3. **Blockchain Access Control Module**
   - Smart contracts for access policy enforcement
   - Secure storage of access control policies
   - Support for direct and indirect file sharing
   - Real-time permission revocation

4. **Cloud Storage and Encryption Module**
   - Secure file upload with AES encryption
   - Blockchain-verified access controls
   - Decryption for authorized downloads

### Data Structure Design

<div align="center">

| Data Structure | Purpose |
|:-------------:|:-------------:|
| **Merkle Trees** | Secure verification of user credentials using SHA-256 |
| **Solidity Mappings** | Storage of user credentials, roles, and permissions |
| **Linked Lists** | Blockchain structure for immutable records |
| **Byte Arrays** | Processing data in chunks for AES encryption |
| **Key-Value Store** | Storage of encrypted file keys |
| **Hash Tables** | Management of hashed user credentials |
| **Access Control Matrix** | Mapping users to specific file permissions |
| **Role Hierarchy (Tree)** | Hierarchical structure for RBAC |

</div>

## 🔐 Security Mechanisms

### AES Encryption Process
FortiBlock implements AES encryption with the following process:

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/aes_process.png" alt="AES Process" width="650px">
</div>

1. Key Generation (128, 192, or 256 bits)
2. File division into fixed-size blocks
3. Application of substitution-permutation network:
   - SubBytes (S-Box substitution)
   - ShiftRows (cyclic shifting)
   - MixColumns (mathematical transformation)
   - AddRoundKey (XOR with round key)
4. Multiple round iterations based on key size
5. Final ciphertext generation
6. Secure encrypted file storage

### SHA-256/512 for Credential Protection

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/sha_process.png" alt="SHA Process" width="650px">
</div>

1. User registration with secure password hashing
2. Smart contract storage of irreversible credential hashes
3. Secure authentication through hash comparison
4. Immutable access attempt logging

## 📊 Results and Demonstrations

### System Interface

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/welcome_page.png" alt="Welcome Page" width="750px">
  <p><em>FortiBlock welcome interface</em></p>
</div>

### Data Owner Dashboard

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/owner_dashboard.png" alt="Data Owner Dashboard" width="750px">
  <p><em>Upload and access control management interface</em></p>
</div>

### Data User Access

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/user_access.png" alt="Data User Access" width="750px">
  <p><em>Secure file access and download interface</em></p>
</div>

### Indirect Sharing

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/indirect_sharing.png" alt="Indirect Sharing" width="750px">
  <p><em>Controlled indirect access sharing mechanism</em></p>
</div>

### Revocation Management

<div align="center">
  <img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/revocation.png" alt="Revocation Dashboard" width="750px">
  <p><em>Access revocation interface with cascade effect</em></p>
</div>

## 🌐 Applications

<div align="center">

| Sector | Application |
|:-------------:|:-------------:|
| **Enterprise** | Secure cloud storage for sensitive corporate data |
| **Education** | Protected management of student records and research data |
| **Healthcare** | Privacy-preserving handling of patient medical records |
| **Government** | Tamper-proof management of sensitive citizen data |
| **Collaboration** | Controlled access to shared resources across organizations |

</div>

## 🚀 Future Scope

<div align="center">

| Enhancement | Description |
|:-------------:|:-------------:|
| **Multi-cloud Integration** | Expand support for multiple cloud providers |
| **AI-powered Access Control** | Implement machine learning for dynamic permission adjustment |
| **Real-time Threat Detection** | Develop anomaly detection for suspicious activities |
| **Quantum-resistant Cryptography** | Upgrade encryption for protection against quantum threats |

</div>

## 👥 Team Members

<div align="center">

| Name | Role | Contribution | GitHub |
|:------:|:------:|:--------------|:--------:|
| **Sunil R** (Team Lead) | Full Stack Developer | Project coordination, Backend implementation, Cloud integration | [GitHub](https://github.com/SunilRavi7) |
| **Shivakumar** | Security Specialist | Cryptography implementation, Security protocols | [GitHub](https://github.com/Shivakumarmathpati) |
| **Surya Bharadwaj B S** | Blockchain Developer | Smart contract development, Blockchain integration | [GitHub](https://github.com/username) |
| **Rohan A Murari** | Frontend Designer | UI/UX design, Frontend implementation, Documentation | [GitHub](https://github.com/username) |

</div>

## 📚 Project Documentation

<div align="center">

### Access Complete Project Report

<img src="https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Results/qr_code.png" alt="Project Report QR Code" width="250px">

[Download Full Project Report](https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment/blob/main/Documentation/FortiBlock_Project_Report.pdf)

</div>

## 🙏 Acknowledgements
We extend our sincere gratitude to:
- Dr. Manjunath H and Dr. Bhanushree K J for their constant guidance and support
- Dr. Girija J, HOD, Department of Computer Science & Engineering, Bangalore Institute of Technology
- Karnataka State Council for Science and Technology (KSCST) for recognizing and sponsoring our project

## 📬 Contact

<div align="center">

**For inquiries and collaboration opportunities:**

📧 **Email:** [sunilr31r@gmail.com](mailto:sunilr31r@gmail.com)

💼 **LinkedIn:** [Sunil R](https://www.linkedin.com/in/sunil-r-1234567890/)

🌐 **Project Repository:** [FortiBlock GitHub](https://github.com/SunilRavi7/FortiBlock_A-Hybrid-Blockchain-Framework-for-Secure-Cloud-Access-Data-Environment)

</div>

---

<div align="center">
<p style="font-family: 'Cambria', serif; font-size: 16px;">© 2024 FortiBlock Team | Developed at Bangalore Institute of Technology</p>
</div>
