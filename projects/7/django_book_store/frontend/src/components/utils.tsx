export class Regex {
  static inputPassword(inputString: string): string {
    return inputString.replace(
      /[^a-zA-Z0-9@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/g,
      "",
    );
  }

  static inputPassword2(inputString: string): string {
    return inputString.replace(/[^a-zA-Z0-9]/g, "");
  }
}

export class LocalStorage {
  static get(key: string) {
    try {
      const storedValue = localStorage.getItem(key);
      if (storedValue !== null) {
        return JSON.parse(storedValue);
      } else {
        return null;
      }
    } catch (error) {
      console.error(`Ошибка при чтении из локального хранилища: ${error}`);
      return null;
    }
  }
  static set(key: string, value: any) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(`Ошибка при записи в локальное хранилище: ${error}`);
    }
  }

  static remove(key: string) {
    try {
      localStorage.removeItem(key);
    } catch (error) {
      console.error(
        `Ошибка при удалении элемента из локального хранилища: ${error}`,
      );
    }
  }
}
