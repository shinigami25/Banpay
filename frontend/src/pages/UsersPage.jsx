import { useEffect, useState } from "react";
import api from "../api";

const ROLES = ["admin", "films", "people", "locations", "species", "vehicles"];

export default function UsersPage() {
  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({ username: "", role: "films", password: "" });
  const [editingId, setEditingId] = useState(null);
  const [error, setError] = useState("");

  const fetchUsers = async () => {
    try {
      const { data } = await api.get("/users/");
      setUsers(data);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to load users");
    }
  };

  useEffect(() => { fetchUsers(); }, []);

  const resetForm = () => {
    setForm({ username: "", role: "films", password: "" });
    setEditingId(null);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      if (editingId) {
        const payload = {};
        if (form.username) payload.username = form.username;
        if (form.role) payload.role = form.role;
        if (form.password) payload.password = form.password;
        await api.put(`/users/${editingId}`, payload);
      } else {
        await api.post("/users", form);
      }
      resetForm();
      fetchUsers();
    } catch (err) {
      setError(err.response?.data?.detail || "Operation failed");
    }
  };

  const handleEdit = (user) => {
    setEditingId(user.id);
    setForm({ username: user.username, role: user.role, password: "" });
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this user?")) return;
    try {
      await api.delete(`/users/${id}`);
      fetchUsers();
    } catch (err) {
      setError(err.response?.data?.detail || "Delete failed");
    }
  };

  return (
    <div>
      <h2>Users</h2>
      {error && <p style={styles.error}>{error}</p>}

      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          placeholder="Username"
          value={form.username}
          onChange={(e) => setForm({ ...form, username: e.target.value })}
          style={styles.input}
          required={!editingId}
        />
        <select
          value={form.role}
          onChange={(e) => setForm({ ...form, role: e.target.value })}
          style={styles.input}
        >
          {ROLES.map((r) => <option key={r} value={r}>{r}</option>)}
        </select>
        <input
          type="password"
          placeholder={editingId ? "New password (optional)" : "Password"}
          value={form.password}
          onChange={(e) => setForm({ ...form, password: e.target.value })}
          style={styles.input}
          required={!editingId}
        />
        <button type="submit" style={styles.btn}>
          {editingId ? "Update" : "Create"}
        </button>
        {editingId && (
          <button type="button" onClick={resetForm} style={styles.cancelBtn}>
            Cancel
          </button>
        )}
      </form>

      <table style={styles.table}>
        <thead>
          <tr>
            <th style={styles.th}>Username</th>
            <th style={styles.th}>Role</th>
            <th style={styles.th}>Created</th>
            <th style={styles.th}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.id}>
              <td style={styles.td}>{u.username}</td>
              <td style={styles.td}>{u.role}</td>
              <td style={styles.td}>{new Date(u.creation_date).toLocaleDateString()}</td>
              <td style={styles.td}>
                <button onClick={() => handleEdit(u)} style={styles.editBtn}>Edit</button>
                <button onClick={() => handleDelete(u.id)} style={styles.deleteBtn}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const styles = {
  error: { color: "#e94560" },
  form: { display: "flex", gap: "8px", marginBottom: "24px", flexWrap: "wrap" },
  input: { padding: "8px 12px", borderRadius: "4px", border: "1px solid #ccc", fontSize: "14px" },
  btn: { padding: "8px 16px", background: "#0f3460", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" },
  cancelBtn: { padding: "8px 16px", background: "#666", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" },
  table: { width: "100%", borderCollapse: "collapse" },
  th: { textAlign: "left", padding: "10px", borderBottom: "2px solid #ddd", background: "#f5f5f5" },
  td: { padding: "10px", borderBottom: "1px solid #eee" },
  editBtn: { marginRight: "8px", padding: "4px 12px", background: "#0f3460", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" },
  deleteBtn: { padding: "4px 12px", background: "#e94560", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" },
};
