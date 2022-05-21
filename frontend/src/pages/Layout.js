import { AppShell, Header, Text, Button, Grid, Modal } from "@mantine/core";
import { useState } from "react";
import { Link } from "react-router-dom";
import { AuthForm } from "../components/AuthForm";

export const Layout = () => {
  const [opened, setOpened] = useState(false);

  return (
    <AppShell
      padding="md"
      header={
        <Header height={60} p="sm">
          <Grid>
            <Grid.Col lg={10} md={8}>
              <Text size="xl" weight={700} component={Link} to="/">
                Hospital Management System
              </Text>
            </Grid.Col>

            <Modal
              opened={opened}
              onClose={() => setOpened(false)}
              title="Register / Login"
            >
              <AuthForm noShadow noPadding />
            </Modal>

            <Grid.Col lg={2} md={2}>
              <Button onClick={() => setOpened(true)}>Register Patient</Button>
            </Grid.Col>
          </Grid>
        </Header>
      }
    ></AppShell>
  );
};
