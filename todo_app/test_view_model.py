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


def test_in_progress_items():
    # Test Case Setup
    items = []
    to_do_item = TodoItem("1", "Test To Do", "To Do")
    items.append(to_do_item)

    in_progress_item = TodoItem("2", "Test In Progress", "In Progress")
    items.append(in_progress_item)

    done_item = TodoItem("3", "Test Done", "Done")
    items.append(done_item)
    view_model = ViewModel(items)
    # End Test Case Setup

    # Start Testing...
    result: list[TodoItem] = view_model.in_progress_items

    # Checking everything worked
    assert len(result) == 1
    item = result[0]
    assert item.status == "In Progress"
    assert result == [in_progress_item]


def test_done_items():
    # Test Case Setup
    items = []
    to_do_item = TodoItem("1", "Test To Do", "To-Do")
    items.append(to_do_item)

    in_progress_item = TodoItem("2", "Test In Progress", "In Progress")
    items.append(in_progress_item)

    done_item = TodoItem("3", "Test Done", "DONE!")
    items.append(done_item)
    view_model = ViewModel(items)
    # End Test Case Setup

    # Start Testing...
    result: list[TodoItem] = view_model.done_items

    # Checking everything worked
    assert len(result) == 1
    item = result[0]
    assert item.status == "DONE!"
    assert result == [done_item]
