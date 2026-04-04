const API_BASE_URL = "http://109.87.156.203:33880";

export async function registerUser({ email, full_name, clear_password }) {
  const response = await fetch(`${API_BASE_URL}/accounts/create`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      full_name,
      clear_password,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data?.detail?.[0]?.msg || "Ошибка регистрации");
  }

  return data;
}

export async function loginUser({ email, password }) {
  const response = await fetch(`${API_BASE_URL}/accounts/auth`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data?.detail?.[0]?.msg || "Ошибка авторизации");
  }

  return data;
}