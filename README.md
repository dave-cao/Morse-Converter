<h1 align='center'>🕵️ Morse Converter</h1>

<h4 align='center'>A program to convert strings into morse code and vice versa</h4>

<br>

![Morse Converter Gif](./assets/morse-converter.gif)

- [Live](https://youtu.be/Ji2s_ZOcDSs) demonstration video.
- [Demo](https://replit.com/@KingCao/Morse-Converter?v=1) the Project.


<!-- ABOUT THE PROJECT -->
## About The Project

A python script that turns strings and text files into morse code. It can also retake in it's morse output to give you back readable English. If you're not familiar with Morse code, [click](https://en.wikipedia.org/wiki/Morse_code) here.

Why? Well, no reason at all. I thought it would be cool to have a secret cypher converter like this in my back pocket in case I get chased down by the FBI and need to use encrypted messages. Sure, there are other more secure cyphers out there, but Morse code is just cool okay.

### Built With

Python3. That's it.

<!-- GETTING STARTED -->
## Getting Started

The following instructions will help you get set up locally. Don't hesitate to message me if you have any problems!

### Prerequisites

- [python 3](https://www.python.org/downloads/)
- The [python installer package installer](https://pip.pypa.io/en/stable/installation/): `pip` (used to install required dependencies)
```sh
python -m ensurepip --upgrade
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/dave-cao/Morse-Converter.git
```

<!-- USAGE EXAMPLES -->
## Usage

There are two ways you can interact with this program.
1. No extra arguments: if no extra arguments are given, the program will prompt you for a string to convert.

```sh
python3 main.py
```
![No extra args given image](img/image0.png)

2. An extra argument was given: this is a text file you want to convert. It will create a new file prefixed with "morse" or "english" and give you the desired output in another text file. Eg:
```sh
# inputted command
python3 main.py moby10b.txt

# output
morse_moby10b.txt
```
3. Exit application
```
ctl + c
```

_For a more comprehensive example of using this application, refer to this [video](https://youtu.be/Ji2s_ZOcDSs)_




<!-- ROADMAP -->
## Roadmap
No current future plans for this project. It's a small project what can I say. However, if you want to improve this code, there are some challenges I encountered.
1. Morse code doesn't have a distinction between lower and upper case letters, therefore, when converting everything back to English, it will only output lowercase letters.
2. Following the above, letters like "I" and "I'm" will all be lower cased
3. If a non morse file contains morse like characters like "**", that will be converted into English when converting back.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request




<!-- CONTACT -->
## Contact

#### David Cao
- Email: sirdavidcao@gmail.com
- [Youtube](https://www.youtube.com/channel/UCEnBPbnNnqhQIIhW1uLXrLA)
- [Linkedin](https://www.linkedin.com/in/david-cao99/)
- Personal Website: https://davidcao.xyz/
- Project Link - https://github.com/dave-cao/Morse-Converter


