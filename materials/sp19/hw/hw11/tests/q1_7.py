test = {
  'name': 'Question 1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure two_minutes_wait is a single value
          >>> isinstance(two_minutes_wait, float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(two_minutes_wait, 54.933679813020404)
          True
          """,
          'hidden': True,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
