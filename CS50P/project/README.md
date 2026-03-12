# International Item Management List
#### Video Demo: <(https://youtu.be/hiloUCGxwjk)>
## Description:
This project was developed in Distrito Federal, Brazil to be an easy way to list items for various purposes, primarily for selling. The key difference is that it has a built-in translator made with the [deep_translator](https://pypi.org/project/deep-translator/) library, translating all your items to new language so you don't need to do it manually, also a currency converter made with the [CurrencyConverter](https://pypi.org/project/CurrencyConverter/) library, which modifies all your items to the new currency and prices accordingly to the current conversion rates,  for potencially selling the items for more than one region/country. Finnaly, printing the list in text format, and for a more professional usage, a docx file too called "**CS50P_Project docx.docx**", made using the [python-docx](https://pypi.org/project/python-docx/) library.

Using the program is simple: Just type all the characteristics of your item (name, description, currency, and price), and keep repeating until you have listed all of them. Your list will be printed in text and docx called "**CS50P_Project docx.docx**" form, and then you will be prompted with a question if you want to modify it or not. If yes, there will be multiple choices you can make to do so, like changing the item's characteristics, translating to another language, etc.

## Notes of the Development Process:
As a new programmer, at first, I was overwhelmed by the scope of the project, it took me a long time to think of an idea that seemed challenging, useful, and possible for me to do. This topic will be a collection of relevant notes on the development progression I did with this final project for CS50P and other technical notes.

At first, I encountered my first problem, I didn't know how to make it so all the characteristics of an item are intertwined and to a lesser scale, to the other items of the list, and also me to iterate them and modify them. But, I found that using a list of dicts, with lists in them, and calling them with Key, and Value in conjunction with the .items and .pop functions, I could make all of that happen, even though it wasn't a very easy process.

To make my project more intuitive, the choices, I used a very basic ASCII, with triple quotation marks, and a function that prints the characteristics and you can simply type in front of it to change it, or not if you don't want to.

To increase the flexibility of the project I also polished it, added protective measures for invalid inputs, and a docx output for the list.

## Project Files:
#### project.py - Project code file
#### requirements.md - Libraries required for the project
#### test_project.py - Project tester using Pytest

## About the Developer:
Hi! My name is Edson, I live in Brazil and I'm on my never-ending way to being the best programmer I can be, for sure this project will be the first of many, including others related to CS50 courses that I want to participate.
