@UI
Feature: Todo Lists

	Background:
		Given I am on the todo page

	Scenario: Creating a todo
		When I type the todo "Do Things!"
		Then todo list item 1 has text "Do Things!"

	Scenario Outline: Creating another todos
		When I type the todo <todo_text>
		Then todo list item <index> has text <todo_text>

		Examples:
			| todo_text | index |
			| Holi      | 1     |
			| Holita    | 1     |

	Scenario: Creating some todos
		When I type the todos '["Holi", "Holita"]'
		Then todo list items '[1, 2]' have the texts '["Holi", "Holita"]'
