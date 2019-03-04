test = {
  'name': 'q1_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(simulated_statistics) == 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(simulated_statistics <= 30)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(simulated_statistics >= 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
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
