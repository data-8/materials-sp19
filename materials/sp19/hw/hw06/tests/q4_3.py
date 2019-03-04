test = {
  'name': 'q4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(maximums) != 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(maximums) == 5000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> max(maximums) <= max(earthquakes.column('mag'))
          True
          """,
          'hidden': False,
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
