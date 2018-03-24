from caseconverter import caseConverter

emptyStr = "Either user given string or case or both empty"

intStr = "It is a not a string value"

assert caseConverter("hello world", "camelcase") == "helloWorld", "Test failed"
assert caseConverter("hello world", "snakecase") == "hello-world", "Test failed"
assert caseConverter("helLO WoRld", "camelcase") == "helloWorld", "Test failed"
assert caseConverter("helLO WoRld", "snakecase") == "hello-world", "Test failed"
assert caseConverter("", "") == emptyStr, "Test failed"
assert caseConverter("hello world", "") == emptyStr, "Test failed"
assert caseConverter("", "snakecase") == emptyStr, "Test failed"
assert caseConverter("", "camelcase") == emptyStr, "Test failed"
assert caseConverter(123, "camelcase") == intStr, "Test failed"
assert caseConverter(123, "snakecase") == intStr, "Test failed"
assert caseConverter("123", "camelcase") == intStr, "Test failed"
assert caseConverter("123", "snakecase") == intStr, "Test failed"
assert caseConverter(["a", "b", "c"], "camelcase") == "aBC", "Test failed"

#### or

import caseconverter as cc

emptyStr = "Either user given string or case or both empty"

intStr = "It is a not a string value"

assert cc.caseConverter("hello world", "camelcase") == "helloWorld", "Test failed"
assert cc.caseConverter("hello world", "snakecase") == "hello-world", "Test failed"
assert cc.caseConverter("helLO WoRld", "camelcase") == "helloWorld", "Test failed"
assert cc.caseConverter("helLO WoRld", "snakecase") == "hello-world", "Test failed"
assert cc.caseConverter("", "") == emptyStr, "Test failed"
assert cc.caseConverter("hello world", "") == emptyStr, "Test failed"
assert cc.caseConverter("", "snakecase") == emptyStr, "Test failed"
assert cc.caseConverter("", "camelcase") == emptyStr, "Test failed"
assert cc.caseConverter(123, "camelcase") == intStr, "Test failed"
assert cc.caseConverter(123, "snakecase") == intStr, "Test failed"
assert cc.caseConverter("123", "camelcase") == intStr, "Test failed"
assert cc.caseConverter("123", "snakecase") == intStr, "Test failed"
assert cc.caseConverter(["a", "b", "c"], "camelcase") == "aBC", "Test failed"

