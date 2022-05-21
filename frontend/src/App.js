import { MantineProvider } from "@mantine/core";
import { Routes, Route } from "react-router-dom";
import { Layout } from "./pages/Layout";

export const App = () => {
  return (
    <MantineProvider
      theme={{ colorScheme: "light" }}
      withGlobalStyles
      withNormalizeCSS
    >
      <Layout></Layout>
      <Routes>
        <Route path="/" />
      </Routes>
    </MantineProvider>
  );
};
