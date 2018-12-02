# ISLR-cauldron
An Introduction to Statistical Learning (James, Witten, Hastie, Tibshirani, 2013): Python code. Inspired by `https://github.com/JWarmenhoven/ISLR-python`

This repository has all the exercises the `An Introduction to Statistical Learning` has in `R` but in `python`. The difference of this repository from `ISLR-python` is that instead of using Jupiter Notebooks, it will use [Cauldron](http://www.unnotebook.com/), `the unnotebook`. 

`Cauldron` provides a lot of benefits when compared to Jupiter Notebooks, it allows the user to: 
- Use his preferred editor. This will allow the user to get all the benefits from editors like [Pycharm](https://www.jetbrains.com/pycharm/).
- Code reviews are made easy. Instead of using blob file, it uses `.py` files. This will allow a smooth code review. 
- `Cauldron` is also ready for production. The user can use it's `CLI` to deploy their notebooks to production. 

Check all the benefits on [Cauldron](http://www.unnotebook.com/) site. 

`Cauldron` is free and open source!

## Run Notebooks in Docker Container

You can use the docker image in this repo to run your notebooks. This way you 
avoid having to install all the python libraries locally.

This is how you start your container and run your notebooks:

- Run docker-compose up to start container: ```docker-compose up```
- Start `Cauldron` with `http://127.0.0.1:5010`

![](docs/gifs/docker-compose-up.gif)

### Installing new python libraries

- Modify the [requirements.txt](requirements.txt) with the additional libraries.
- Rebuild the container

```bash
docker-compose build
```
