test = {
  'name': 'q3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < min(bootstrap_rrs) <= max(bootstrap_rrs) < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.random.seed(123);
          >>> one_bootstrap_rr()
          0.45051908712124883
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
