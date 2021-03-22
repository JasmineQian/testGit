Feature: Tree

# BUILD TOP-DOWN

Scenario: Add properties to tree
  Given a new tree is created with name default
  When the name of the tree is asked for
  Then default is returned