def test_imports():
    """Test that main modules can be imported"""
    try:
        import src.main
        assert True
    except ImportError as e:
        assert False, f"Import failed: {e}"