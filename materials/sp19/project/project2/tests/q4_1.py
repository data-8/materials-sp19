test = {
  'name': 'q4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> HERS.num_rows == 2763
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> HERS.num_columns == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you label your columns properly.;
          >>> set(np.sort(HERS.labels))
          {'CHD', 'HRT'}
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
