import {
  Form as VeeForm,
  Field as VeeField,
  defineRule,
  ErrorMessage,
  configure,
} from "vee-validate";
import { required, email, min, max } from "@vee-validate/rules/";

export default {
  install(app) {
    app.component("VeeForm", VeeForm);
    app.component("VeeField", VeeField);
    app.component("ErrorMessage", ErrorMessage);
    defineRule("min", min);
    defineRule("max", max);
    defineRule("required", required);
    defineRule("email", email);
    configure({
      generateMessage: (ctx) => {
        const messages = {
          required: `${
            ctx.field[0].toUpperCase() + ctx.field.slice(1)
          } is required.`,
          email: `${
            ctx.field[0].toUpperCase() + ctx.field.slice(1)
          } must be a valid email.`,
        };
        const message = messages[ctx.rule.name]
          ? messages[ctx.rule.name]
          : `${ctx.field[0].toUpperCase() + ctx.field.slice(1)} is invalid.`;
        return message;
      },
      validateOnBlur: true,
      validateOnChange: true,
      validateOnInput: false,
    });
  },
};
