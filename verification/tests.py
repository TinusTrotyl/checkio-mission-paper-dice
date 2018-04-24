"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
                '      ',
                ' 1    ',
                ' 2354 ',
                ' 6    ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '2354',
                ' 6  ',
                '    ',
                ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '2354',
                '  6 ',
                '    ',
                ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '2354',
                '   6',
                '    ',
                ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                ' 1  ',
                '2354',
                ' 6  ',
                '    ',
                ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                ' 1  ',
                '2354',
                '  6 ',
                '    ',
                ],
            "answer": True,
        },
        {
            "input": [
                '    ',
                '1   ',
                '235 ',
                '  64',
                '    ',
                ],
            "answer": True,
        }, 
        {
            "input": [
                '    ',
                ' 1  ',
                '235 ',
                '  64',
                '    ',
                ],
            "answer": True,
        }, 
        {
            "input": [
                '      ',
                '   1  ',
                ' 235  ',
                '   64 ',
                '      ',
                ],
            "answer": True,
        }, 
        {
            "input": [
                '       ',
                ' 126   ',
                '   354 ',
                '       ',
                ],
            "answer": True,
        }, 
        {
            "input": [
                '      ',
                ' 12   ',
                '  36  ',
                '   54 ',
                '      ',
                ],
            "answer": True,
        }, 
    ],
    "Rotate": [
        {
            "input": [
                '     ',
                ' 126 ',
                '  3  ',
                '  5  ',
                '  4  ',
                '     ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                '    6 ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '     ',
                '  4  ',
                '  5  ',
                '  3  ',
                ' 621 ',
                '     ',
                ],
            "answer": True,
        },
        {
            "input": [
                '     ',
                '  21 ',
                '  3  ',
                '  5  ',
                ' 64  ',
                '     ',
                ],
            "answer": True,
        },
        {
            "input": [
                '     ',
                '   1 ',
                '  32 ',
                ' 56  ',
                ' 4   ',
                '     ',
                ],
            "answer": True,
        },
    ],
    "Reverse": [
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                '   6  ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                '  6   ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                ' 4532 ',
                ' 6    ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   1  ',
                ' 4532 ',
                '  6   ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '    1 ',
                '  532 ',
                ' 46   ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   1  ',
                '  532 ',
                ' 46   ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '  1   ',
                '  532 ',
                ' 46   ',
                '      ',
                ],
            "answer": True,
        },
        {
            "input": [
                '       ',
                '   621 ',
                ' 453   ',
                '       ',
                ],
            "answer": True,
        },
        {
            "input": [
                '      ',
                '   21 ',
                '  63  ',
                ' 45   ',
                '      ',
                ],
            "answer": True,
        },
    ],
    "Wrong": [
        {
            "input": [
                '     ',
                ' 12  ',
                '  3  ',
                '  4  ',
                '  56 ',
                '     ',
                ],
            "answer": False,
        },
        {
            "input": [
                '      ',
                ' 12   ',
                '  34  ',
                '   56 ',
                '      ',
                ],
            "answer": False,
        },
        {
            "input": [
                '      ',
                ' 1  6 ',
                ' 2354 ',
                '      ',
                ],
            "answer": False,
        },
        {
            "input": [
                '      ',
                ' 1    ',
                ' 2    ',
                ' 6354 ',
                '      ',
                ],
            "answer": False,
        },
        {
            "input": [
                '     ',
                ' 12  ',
                '  36 ',
                '   5 ',
                '   4 ',
                '     ',
                ],
            "answer": False,
        },
    ],
}
