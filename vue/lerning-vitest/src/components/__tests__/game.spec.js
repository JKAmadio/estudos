import { spyOn } from "@vitest/spy";
import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import Game from '../Game.vue';
import Navbar from '../Navbar.vue';
import Login from '../Login.vue';

describe('interaction Navbar - Game', () => {
  it('method methodUpdateShowLogin is called on updateShowLogin is emited', () => {
    const methodUpdateShowLogin = spyOn(Game.methods, 'methodUpdateShowLogin');
    const wrapper = mount(Game, {
      data() {
        return {
          showLogin: false
        };
      }
    });

    wrapper.findComponent(Navbar).vm.$emit('updateShowLogin');
    expect(methodUpdateShowLogin).toHaveBeenCalled();
  });

  it('showLogin is oposite when methodUpdateShowLogin is called', () => {
    const methodUpdateShowLogin = spyOn(Game.methods, 'methodUpdateShowLogin');
    const wrapper = mount(Game, {
      data() {
        return {
          showLogin: false
        };
      }
    });

    wrapper.findComponent(Navbar).vm.$emit('updateShowLogin');
    expect(methodUpdateShowLogin).toHaveBeenCalled();
    expect(wrapper.vm.showLogin).toBe(true);
  });
});

describe('interaction Login - Game', () => {
  it('isLogged turns true on updateIsLogged', () => {
    const wrapper = mount(Game, {
      data () {
        return {
          showLogin: true, //importante colocar esse para que o componente Login exista
          isLogged: false
        };
      }
    });

    wrapper.findComponent(Login).vm.$emit('updateIsLogged');
    expect(wrapper.vm.isLogged).toBe(true);
  });
});

