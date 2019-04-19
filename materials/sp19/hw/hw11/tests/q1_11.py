test = {
  'name': 'Question 1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lower_bound > 80
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> upper_bound < 955
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> lower_bound > 94 and upper_bound < 101
          True
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
