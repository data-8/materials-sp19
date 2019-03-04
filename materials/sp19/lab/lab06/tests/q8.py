test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(simulated_statistics) == 1000
          True
          >>> np.all(simulated_statistics <= 30)
          True
          >>> np.all(simulated_statistics >= 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Double check your simulation_and_statistic function!
          >>> # It might be returning the wrong value.
          >>> 0 <= simulation_and_statistic(210, model_proportions, expected_correct) <= 25
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
