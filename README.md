# Dynastatic NFT Generator

Light (but slow) NFT image and metadata generator that uses static assets for some parts of the generation and dynamic assets for others. It additionally supports semi-static folders, where, for example, each NFT needs assets from a specific path but the assets it layers on top of those are dynamic.

## To use

```
git clone https://github.com/dylanireland/dynastatic-nft-image-generator.git
cd dynastic-nft-image-generator/
python3 generator.py
```
Place your visual NFT assets in the same working directory.
Remember to adjust your paths and layers within *generate.py* to your use case.
Tested support for Python version 3.9.12, untested on other Python versions.
