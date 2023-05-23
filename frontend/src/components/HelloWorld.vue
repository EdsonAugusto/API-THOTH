<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-col class="mb-2">
          <v-row>
              <v-expansion-panels
                v-model="panel"
                :disabled="disabled"
                multiple
              >
                <v-col cols="12" class="pa-0 ma-0" style="text-align: center;">
                  <v-card
                  >
                    <v-card-title >
                      CONTATOS & RAMAIS INTERNOS
                    </v-card-title >

                    <v-card-text class="text-center">
                      <v-row >
                      <v-col class="pa-2 ma-1"
                  sm="6"
                  offset-sm="0"
                  md="5"
                  offset-md="0"
                >
                  <v-sheet class="m-0" style="border-radius: 9%;">
                    <v-expansion-panel>
                      <v-expansion-panel-title class="bg-info" expand-icon="mdi-cog" collapse-icon="mdi-minus" style="text-align: center; padding-left: 10%; padding-right: 10%; color: white;">
                        <strong style="padding-right: 5px">UTILIDADES</strong>
                      </v-expansion-panel-title>
                      <v-expansion-panel-text>
                        <v-table class="table-strip" density="compact" hover>
                          <thead> 
                            <tr>
                              <th class="text-center"><strong>Botão</strong></th>
                              <th class="text-left">Função botão no ramal</th>
                            </tr>
                          </thead>
                          <tbody density="compact">
                            <tr>
                              <td><strong>#</strong></td>
                              <td class="text-left" style="{size: 6px;}">
                                <strong>•</strong> Puxar ligação do seu setor.<br>
                                <strong>•</strong> Transferir uma ligação com anúncio para o ramal discado.
                              </td>
                            </tr>
                            <tr>
                              <td><strong>*</strong></td>
                              <td class="text-left"><strong>•</strong> Tranferir ligação sem anúncio.</td>
                            </tr>
                          </tbody>
                        </v-table>
                      </v-expansion-panel-text>
                    </v-expansion-panel>
                  </v-sheet>
                </v-col>
                <v-col class="pa-2 ma-1"
                  sm="6"
                  offset-sm="0"
                  md="5"
                  offset-md="0"
                >
                  <v-sheet class="m-0" style="border-radius: 9%;">
                    <v-expansion-panel>
                      <v-expansion-panel-title class="bg-alert" color="error" expand-icon="mdi-alert-circle" collapse-icon="mdi-minus" style="text-align: center;">
                        Avisos
                      </v-expansion-panel-title>
                      <v-expansion-panel-text>
                        <v-table density="compact" hover>
                          <tbody density="compact">
                            <tr>
                              <td><strong>1º</strong></td>
                              <td class="text-left" style="{size: 6px;}">
                                Não forneça contatos internos sem autorização previa de um responsável.
                              </td>
                            </tr>
                          </tbody>
                        </v-table>
                        <v-list lines="three">
                          <v-list-item-subtitle class="text-left">
                            
                          </v-list-item-subtitle>
                        </v-list>
                      </v-expansion-panel-text>
                    </v-expansion-panel>
                  </v-sheet>
                </v-col>
              </v-row>
                    </v-card-text>
                  </v-card>
                </v-col>
                
              </v-expansion-panels>
          </v-row>
        </v-col>
        <v-row class="justify-center text-center">
          <v-col cols="12">
            <v-table v-model="selected" fixed-header hover density="compact" style="background-color:bisque">
              <thead>
                <tr>
                  <th class="text-center">Nome</th>
                  <th class="text-center">Setor</th>
                  <th class="text-center">Email</th>
                  <th class="text-center">Corporativo</th>
                  <th class="text-center">Ramal</th>
                  <th class="text-center"></th>
                  <th class="text-center"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in Extensions" :key="item.id">
                  <td>{{ item.employee }}</td>
                  <td>{{ item.acting_sector }}</td>
                  <td>{{ item.employee_email }}</td>
                  <td>{{ item.employee_phone.slice(3) }}</td>
                  <td>{{ item.branch_line }}</td>
                  <td></td>
                  <td></td>
                </tr>
              </tbody>
            </v-table>
          </v-col>
        </v-row>
        
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    selected: [],
    Extensions: [],
    panel: [],
    disabled: false,
    readonly: false,
  }),
  mounted() {
    this.getExtensions();
  },
  methods: {
    getExtensions() {
      axios.get("http://140.1.53.59:8000/api/extensions/").then((response) => {
        this.Extensions = response.data;
      });
    },
  },
};
</script>
