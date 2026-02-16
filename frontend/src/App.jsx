import { Routes, Route, Navigate, Link } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import LoginPage from "./pages/LoginPage";
import UsersPage from "./pages/UsersPage";
import GhibliPage from "./pages/GhibliPage";

function ProtectedRoute({ children }) {
  const { token } = useAuth();
  if (!token) return <Navigate to="/login" replace />;
  return children;
}

function Navbar() {
  const { user, logout } = useAuth();
  return (
    <nav style={styles.nav}>
      <div style={styles.links}>
        <Link to="/users" style={styles.link}>Users</Link>
        <Link to="/ghibli" style={styles.link}>Ghibli</Link>
      </div>
      <div style={styles.right}>
        {user && <span style={styles.role}>{user.username} — {user.role}</span>}
        <button onClick={logout} style={styles.logoutBtn}>Logout</button>
      </div>
    </nav>
  );
}

function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main style={styles.main}>{children}</main>
    </>
  );
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/users"
        element={
          <ProtectedRoute>
            <Layout><UsersPage /></Layout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/ghibli"
        element={
          <ProtectedRoute>
            <Layout><GhibliPage /></Layout>
          </ProtectedRoute>
        }
      />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "12px 24px",
    background: "#1a1a2e",
    color: "#fff",
  },
  links: { display: "flex", gap: "16px" },
  right: { display: "flex", alignItems: "center", gap: "16px" },
  role: { color: "#e0e0e0", fontSize: "14px" },
  link: { color: "#e0e0e0", textDecoration: "none", fontWeight: 500 },
  logoutBtn: {
    background: "#e94560",
    color: "#fff",
    border: "none",
    padding: "8px 16px",
    borderRadius: "4px",
    cursor: "pointer",
  },
  main: { padding: "24px", maxWidth: "960px", margin: "0 auto" },
};
