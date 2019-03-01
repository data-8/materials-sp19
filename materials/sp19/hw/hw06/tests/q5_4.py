test = {
  'name': 'q5_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(coin_statistics) == repetitions
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all([0 <= k <= 10 for k in coin_statistics])
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
