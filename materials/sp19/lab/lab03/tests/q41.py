test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Oops, your name is assigned to the wrong data type!
          >>> type(year_population_crossed_6_billion) == int
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> year_population_crossed_6_billion == 1999
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
