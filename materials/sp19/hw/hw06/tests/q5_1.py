test = {
  'name': 'q5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(coin_model_probabilities) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(coin_model_probabilities) == 1
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
