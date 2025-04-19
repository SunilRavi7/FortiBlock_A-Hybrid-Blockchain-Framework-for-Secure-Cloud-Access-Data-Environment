const AuthPrivacyChain = artifacts.require("AuthPrivacyChain");

module.exports = function(deployer) {
  deployer.deploy(AuthPrivacyChain);
};
