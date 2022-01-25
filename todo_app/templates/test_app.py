from todo_app.trello_items import Item
from todo_app.class_viewmodel import ViewModel


def test_todo_items():
    # Test Case Setup
    items = []
    to_do_item = Item("1", "Test To Do", "To-Do")
    items.append(to_do_item)

    in_progress_item = Item("2", "Test In Progress", "In Progress")
    items.append(in_progress_item)

    done_item = Item("3", "Test Done", "DONE!")
    items.append(done_item)
    view_model = ViewModel(items)
    # End Test Case Setup

    # Start Testing...
    result: list[Item] = view_model.to_do_items

    # Checking everything worked
    assert len(result) == 1
    item = result[0]
    assert item.status == "To-Do"
    assert result == [to_do_item]


def test_in_progress_items():
    # Test Case Setup
    items = []
    to_do_item = Item("1", "Test To Do", "To-Do")
    items.append(to_do_item)

    in_progress_item = Item("2", "Test In Progress", "In Progress")
    items.append(in_progress_item)

    done_item = Item("3", "Test Done", "DONE!")
    items.append(done_item)
    view_model = ViewModel(items)
    # End Test Case Setup

    # Start Testing...
    result: list[Item] = view_model.in_progress_items

    # Checking everything worked
    assert len(result) == 1
    item = result[0]
    assert item.status == "In Progress"
    assert result == [in_progress_item]


def test_done_items():
    # Test Case Setup
    items = []
    to_do_item = Item("1", "Test To Do", "To-Do")
    items.append(to_do_item)

    in_progress_item = Item("2", "Test In Progress", "In Progress")
    items.append(in_progress_item)

    done_item = Item("3", "Test Done", "DONE!")
    items.append(done_item)
    view_model = ViewModel(items)
    # End Test Case Setup

    # Start Testing...
    result: list[Item] = view_model.done_items

    # Checking everything worked
    assert len(result) == 1
    item = result[0]
    assert item.status == "DONE!"
    assert result == [done_item]
