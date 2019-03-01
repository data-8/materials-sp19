test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simulate_key_strike() is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import string;
          >>> all([simulate_key_strike() in string.ascii_lowercase for i in range(100)])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np;
          >>> 26 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 20
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
