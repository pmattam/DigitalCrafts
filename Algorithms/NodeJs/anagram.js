const fs = require('fs');
const assert = require('assert');
const promisify = require('util').promisify;
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

let fileName = 'words.txt';
let file = 'anagram.txt'

let anagram = fileName => {
    readFile(fileName)
        .then(data => {
            var wordsObj = {};
            var anagramsObj = {};
            var wordsList = data.toString().replace(/"/g, "").split(",");
            wordsList.forEach(word => {
                wordsObj[word.length] === undefined ? wordsObj[word.length] = [word] : wordsObj[word.length].push(word);
            });
            Object.keys(wordsObj).forEach(key => {
                wordsObj[key].forEach((checkWord, index) => {
                    var wordCompareList = wordsObj[key].slice(index + 1);
                    wordCompareList.forEach(nextWord => {
                        if (isAnagram(checkWord, nextWord)) {
                            anagramsObj[checkWord] === undefined ? anagramsObj[checkWord] = [nextWord] : anagramsObj[checkWord].push(nextWord);
                        }
                    });
                });
            });
            console.log("anagramObj", anagramsObj);
            return anagramsObj;
        })
        .then(anagramsObj => {
            writeFile(file, JSON.stringify(anagramsObj));
        })
};

let isAnagram = (firstWord, secondWord) => {
    var firstWord = firstWord.split("").sort().join("");
    var secondWord = secondWord.split("").sort().join("");
    return firstWord === secondWord;
};
assert.deepStrictEqual(isAnagram("care", "race"), true, "Test failed");

anagram(fileName);