test = {
  'name': 'q5_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_heads = coin_simulation_and_statistic(10, coin_model_probabilities);
          >>> 0 <= num_heads <= 10
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
