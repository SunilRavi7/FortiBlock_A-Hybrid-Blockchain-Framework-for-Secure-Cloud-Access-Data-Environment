# FortiBlock: Hybrid Blockchain Framework for Secure Access Control in Cloud Environment

<!-- Add Project Logo/Banner Image Here -->
![FortiBlock Banner](https://place-for-your-banner-image.png)

## 🎉 Award Recognition
We are thrilled to share that FortiBlock has been **selected for sponsorship** under the **48th Series of Student Project Programme (SPP) 2024-25** by the **Karnataka State Council for Science and Technology (KSCST)**! 

> Among numerous Deep Learning and Machine Learning projects, FortiBlock stood out as the only Blockchain-based project selected for sponsorship.

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Implementation Details](#implementation-details)
- [Security Mechanisms](#security-mechanisms)
- [Results and Demonstrations](#results-and-demonstrations)
- [Applications](#applications)
- [Future Scope](#future-scope)
- [Team Members](#team-members)
- [Acknowledgements](#acknowledgements)
- [References](#references)

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

![Architecture Flow](https://place-for-your-architecture-image.png)

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

| Component | Technologies |
|-----------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Django, Node.js |
| **Blockchain** | Ethereum, Solidity Smart Contracts, Web3.js |
| **Encryption** | AES (Advanced Encryption Standard) |
| **Authentication** | SHA-256/512 Hashing |
| **Cloud Storage** | IPFS API |
| **Data Structures** | Merkle Trees, Mapping, Linked Lists, Hash Tables |

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

| Data Structure | Purpose |
|----------------|---------|
| **Merkle Trees** | Secure verification of user credentials using SHA-256 |
| **Solidity Mappings** | Storage of user credentials, roles, and permissions |
| **Linked Lists** | Blockchain structure for immutable records |
| **Byte Arrays** | Processing data in chunks for AES encryption |
| **Key-Value Store** | Storage of encrypted file keys |
| **Hash Tables** | Management of hashed user credentials |
| **Access Control Matrix** | Mapping users to specific file permissions |
| **Role Hierarchy (Tree)** | Hierarchical structure for RBAC |

## 🔐 Security Mechanisms

### AES Encryption Process
FortiBlock implements AES encryption with the following process:
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
1. User registration with secure password hashing
2. Smart contract storage of irreversible credential hashes
3. Secure authentication through hash comparison
4. Immutable access attempt logging

## 📊 Results and Demonstrations

### System Interface
![Welcome Page](https://place-for-welcome-page-screenshot.png)
*FortiBlock welcome interface*

### Data Owner Dashboard
![Data Owner Dashboard](https://place-for-dashboard-screenshot.png)
*Upload and access control management interface*

### Data User Access
![Data User Access](https://place-for-data-user-screenshot.png)
*Secure file access and download interface*

### Indirect Sharing
![Indirect Sharing](https://place-for-indirect-sharing-screenshot.png)
*Controlled indirect access sharing mechanism*

### Revocation Management
![Revocation Dashboard](https://place-for-revocation-screenshot.png)
*Access revocation interface with cascade effect*

## 🌐 Applications
- **Enterprise Data Management**: Secure cloud storage for sensitive corporate data
- **Educational Institutions**: Protected management of student records and research data
- **Healthcare Systems**: Privacy-preserving handling of patient medical records
- **Government Agencies**: Tamper-proof management of sensitive citizen data
- **Multi-party Collaborations**: Controlled access to shared resources

## 🚀 Future Scope
- **Multi-cloud Integration**: Expand support for multiple cloud providers
- **AI-powered Access Control**: Implement machine learning for dynamic permission adjustment
- **Real-time Threat Detection**: Develop anomaly detection for suspicious activities
- **Quantum-resistant Cryptography**: Upgrade encryption for protection against quantum threats

## 👥 Team Members

| Name | Role | Contribution | GitHub |
|------|------|--------------|--------|
| **Sunil R** (Team Lead) | Full Stack Developer | Project coordination, Backend implementation, Cloud integration | [GitHub](https://github.com/username) |
| **Shivakumar** | Security Specialist | Cryptography implementation, Security protocols | [GitHub](https://github.com/Shivakumarmathpati) |
| **Surya Bharadwaj B S** | Blockchain Developer | Smart contract development, Blockchain integration | [GitHub](https://github.com/username) |
| **Rohan A Murari** | Frontend Designer | UI/UX design, Frontend implementation, Documentation | [GitHub](https://github.com/username) |

## 🙏 Acknowledgements
We extend our sincere gratitude to:
- Dr. Manjunath H and Dr. Bhanushree K J for their constant guidance and support
- Dr. Girija J, HOD, Department of Computer Science & Engineering, Bangalore Institute of Technology
- Karnataka State Council for Science and Technology (KSCST) for recognizing and sponsoring our project

## 📚 References
1. Zhou, W., Ji, J. (2019). A Blockchain-Based Access Control Framework for Secured Data Sharing in Industrial Internet. IEEE Eighth International Conference on Advanced Cloud and Big Data.
2. Tan, L., Shi, N., Yang, C., Yu, K. (2020). A Blockchain-Based Access Control Framework for Cyber-Physical-Social System Big Data. Global Information and Telecommunication Institute, Waseda University.
3. Lin, X., Li, J., Wu, J., Liang, H., Yang, W. (2019). Making knowledge tradable in edge-AI enabled IoT: A consortium blockchain-based efficient and incentive approach. IEEE Trans. Ind. Informat., 15(12), 6367-6378.
4. Li, W., Wu, J., Cao, J., Chen, N., Zhang, Q., Buyya, R. (2021). Blockchain-based trust management in cloud computing systems: a taxonomy, review and future directions. Qianjiang College, Hangzhou Normal University.
5. Algarni, S., Eassa, F., Almarhabi, K., Almalaise, A., Albassam, E. (2021). Blockchain-Based Secured Access Control in an IoT System. Applied Sciences, 11(4), 1772.

---
© 2024 FortiBlock Team | Developed at Bangalore Institute of Technology
