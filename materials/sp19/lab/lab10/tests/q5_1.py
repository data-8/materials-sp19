test = {
  'name': 'q5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(secrets.split(" ")) == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> secrets.split(" ")[3][-1] == '!'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(secrets.split(" ")[2]) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> (secrets.split(" ")[1][2] + secrets.split(" ")[1][0]).lower() == secrets.split(" ")[2]
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
