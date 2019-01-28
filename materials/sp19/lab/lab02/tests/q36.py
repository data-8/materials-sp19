test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> berkeley_markets.num_rows == 3
          True
          >>> list(berkeley_markets.column('city')) == ['Berkeley', 'Berkeley', 'Berkeley']
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
