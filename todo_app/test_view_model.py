from todo_app.trello_items import TodoItem
from todo_app.view_model import ViewModel


def test_to_do_items_functions_on_view_model_class_doesnt_accept_in_progress_items():
    # Test Case Setup
    items = [
        TodoItem(1, "In Progress Item", "In Progress")
    ]
    view_model = ViewModel(items)

    # Start Testing...
    result = view_model.to_do_items

    # Checking everything worked
    assert len(result) == 0


def test_to_do_items_functions_on_view_model_class_doesnt_accept_done_items():
    # Test Case Setup
    items = [
        TodoItem(1, "Done Item", "DONE!")
    ]
    view_model = ViewModel(items)

    # Start Testing...
    result = view_model.to_do_items

    # Checking everything worked
    assert len(result) == 0


def test_to_do_items_functions_on_view_model_class_does_accept_todo_status_items():
    # Test Case Setup
    items = [
        TodoItem(1, "Todo Item", "To-Do")
    ]
    view_model = ViewModel(items)

    # Start Testing...
    result = view_model.to_do_items

    # Checking everything worked
    assert len(result) == 1
