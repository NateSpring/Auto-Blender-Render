<h1 align="center"><b>AUTO BLENDER RENDER</b></h1>

  <p align="center">Run Blender as a background process to render ".blend" files in a directory via CLI</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

After being tasked with rendering a couple hundred Blender files; I wrote this Python script to loop through folders in a directory and render the .blend files via CLI.
On average this saved 50% of render time compared to manually opening and rendering each file.

### Built With

* Python



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
* python
* blender
```sh
npm install npm@latest -g
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/NateSpring/Auto-Blender-Render.git
```
2. Install NPM packages
```sh
npm install
```
3. Change Directory Paths and Blender application path.



<!-- USAGE EXAMPLES -->
## Usage

Use this project to loop through a directory and render all .blend files to your selected output directory. 
After cloning the repo, modify your input and output direcory paths, including the 'subprocess' location for your Blender installation.
If a folder from the input directory already exists in the ouput directory, it will be skipped to avoid rendering twice.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - Nate Spring

Project Link: [https://github.com/NateSpring/Auto-Blender-Render](https://github.com/NateSpring/Auto-Blender-Render)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=flat-square
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=flat-square
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=flat-square
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=flat-square
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: images/screenshot.png
