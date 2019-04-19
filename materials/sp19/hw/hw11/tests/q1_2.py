test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Ensure your correlation function returns one number between -1 and 1
          >>> abs(correlation(Table().with_columns('a', np.random.normal(0, 1, 10),'b', np.random.normal(0, 1, 10)))) <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(standard_units(np.arange(5)), np.sqrt(2)/2 * np.arange(-2, 3))
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(correlation(faithful), 0.90081116832181318)
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
