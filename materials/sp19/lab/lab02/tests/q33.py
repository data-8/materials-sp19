test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sorted(farmers_markets_locations.labels)
          ['MarketName', 'State', 'city', 'x', 'y']
          >>> farmers_markets_locations.num_rows == 8546
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
