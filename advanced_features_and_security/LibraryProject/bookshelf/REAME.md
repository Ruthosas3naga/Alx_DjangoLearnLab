## Permissions and Groups Setup

### Custom Permissions

The application includes custom permissions for managing `Post` objects:

- `can_view_post`: Allows users to view posts.
- `can_create_post`: Allows users to create new posts.
- `can_edit_post`: Allows users to edit existing posts.
- `can_delete_post`: Allows users to delete posts.

### User Groups

Three user groups are set up to manage access:

1. **Viewers**: Can only view posts.
2. **Editors**: Can view, create, and edit posts.
3. **Admins**: Can view, create, edit, and delete posts.

### Enforcing Permissions

Permissions are enforced using the `@permission_required` decorator in views. For example, the `create_post` view requires the `can_create_post` permission.
