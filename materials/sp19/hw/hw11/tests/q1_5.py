test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lower_end > 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> upper_end < 15
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> upper_end > 9 and lower_end < 12
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
