test = {
  'name': 'Question 1_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure most_recent_wait is a single value
          >>> isinstance(most_recent_wait, float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(most_recent_wait, 97.85224539355451)
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
