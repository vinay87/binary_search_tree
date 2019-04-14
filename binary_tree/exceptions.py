#!/usr/bin/env python
# -*- coding: utf-8 -*-


class InvalidTraversalMode(Exception):
    """Exception raised when the mode isn't acceptable, or
    it isn't anticipated. Right now, the only implemented
    modes are inorder, postorder and preorder."""
    pass
